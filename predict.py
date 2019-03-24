import cv2
import numpy as np
from PIL import ImageGrab
from PIL.Image import LANCZOS
from tkinter import *
from tkinter.colorchooser import askcolor
import tensorflow as tf
from tensorflow import keras

tf.logging.set_verbosity(tf.logging.ERROR)
digits_model = keras.models.load_model('cnn.h5')

# Tkinter drawing app modified from
# https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06
class Paint(object):

    DEFAULT_COLOR = 'white'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='Predict', command=self.activate_button)
        self.pen_button.grid(row=0, column=0)

        self.var = StringVar(master=self.root, value='No value')

        self.value_label = Label(self.root, textvariable=self.var, font=('Arial', 36))
        self.value_label.grid(row=0, column=1)

        self.c = Canvas(self.root, bg='black', width=600, height=600)
        self.c.grid(row=1, columnspan=2)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def activate_button(self):
        img = self.get_img()
        pred_list = digits_model.predict(img).tolist()[0]
        val = np.argmax(pred_list)
        print(val)
        self.var.set(str(val))
        self.reset(None)

    def get_img(self):
        x0=self.root.winfo_rootx()+self.c.winfo_x()
        y0=self.root.winfo_rooty()+self.c.winfo_y()
        x1=x0+self.c.winfo_width()
        y1=y0+self.c.winfo_height()
        img = ImageGrab.grab((x0, y0, x1, y1))
        img = img.resize((28, 28), resample=LANCZOS).convert('L')
        img.save('test.png')
        img = np.asarray(img).reshape(1, 28, 28, 1) / 255
        self.c.delete("all")
        return img

    def paint(self, event):
        paint_color = 'black' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=(50 if self.eraser_on else 20), fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()

# imgs = []
# for i in range(10):
#     img = cv2.imread('test1/%d.png' % i, cv2.IMREAD_GRAYSCALE)
#     img = np.asarray(img, dtype='float32')
#     imgs.append(img)

# imgs = np.asarray(imgs).reshape(10, 28, 28, 1) / 255
# results = digits_model.predict(imgs).tolist()
# print([(np.argmax(r)) for r in results])

# imgs = []
# for i in range(10):
#     img = cv2.imread('test2/%d.png' % i, cv2.IMREAD_GRAYSCALE)
#     img = np.asarray(img, dtype='float32')
#     imgs.append(img)

# imgs = np.asarray(imgs).reshape(10, 28, 28, 1) / 255
# results = digits_model.predict(imgs).tolist()
# print([(np.argmax(r)) for r in results])
# # print('Predicted:', (results.index(1.) + 1))
