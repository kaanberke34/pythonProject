
import tkinter as tk
from sklearn import datasets
import matplotlib.pyplot as plt
import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import numpy as np
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
class Main:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry("700x700")
		self.frame = tk.Frame(self.root)
		self.root.title("Betik Diller Proje Ödevi")
		self.butnew("1- Bar Chart Iris Averages Grafiğini Açmak İçin Tıklayın", "1", Graph1)
		self.butnew("2- Iris Histograms Grafiğini Açmak İçin Tıklayın", "2", Graph2)
		self.butnew("3- Plot 2D Views of the iris dataset Grafiğini Açmak İçin Tıklayın", "3", Graph3)
		self.butnew("4- Bar Chart Setosa Averages Grafiğini Açmak İçin Tıklayın", "4", Graph4)
		self.butnew("5- Scatter Plot Iris Grafiğini Açmak İçin Tıklayın", "5", Graph5)
		self.butnew("6- Sepal Length Histogram Grafiğini Açmak İçin Tıklayın", "6", Graph6)
		self.butnew("7- First Three PCA Directions Grafiğini Açmak İçin Tıklayın", "7", Graph7)
		self.butnew("8- Boxplot Sepal Length Grafiğini Açmak İçin Tıklayın", "8", Graph8)
		self.butnew("9- Boxplot Iris Features Grafiğini Açmak İçin Tıklayın", "9", Graph9)
		self.butnew("10- Iris Histograms for each Flowers Grafiğini Açmak İçin Tıklayın", "10", Graph10)
		self.butnew("11- Scatter Plot for each Flowers Grafiğini Açmak İçin Tıklayın", "11", Graph11)
		self.butnew("12- Histograms of the Features Grafiğini Açmak İçin Tıklayın", "12", Graph12)
		self.butnew("13- Histograms of the Other Features Grafiğini Açmak İçin Tıklayın", "13", Graph13)
		self.butnew("14- All Feature Combinations in One Combined Diagram Grafiğini Açmak İçin Tıklayın", "14", Graph14)
		self.frame.pack()

	def butnew(self, text, number, _class):
		tk.Button(self.frame, text = text, bg="#9999ff", fg="#EFEFF8",font=("Arial", 10,'bold'), command= lambda: self.new_window(number, _class)).pack(fill=tk.X, padx=10, pady=10)
	def new_window(self, number, _class):
		self.new = tk.Toplevel(self.root)
		_class(self.new, number)

class Graph1:
	
	def __init__(self, root, number):

		iris = datasets.load_iris()
		X_iris = iris.data
		Y_iris = iris.target
		n_classes = 3
		averages = [X_iris[Y_iris == i].mean(axis=0) for i in range(n_classes)]
		x = np.arange(len(iris.feature_names))

		fig = plt.figure()
		ax = fig.add_subplot()
		bar1 = ax.bar(x - 0.25, averages[0], 0.25, label=iris.target_names[0])
		br2 = ax.bar(x, averages[1], 0.25, label=iris.target_names[1])
		bar3 = ax.bar(x + 0.25, averages[2], 0.25, label=iris.target_names[2])
		ax.set_xticks(x)
		ax.set_xticklabels(iris.feature_names)

		plt.title("1 - Bar Chart Iris Averages")
		plt.ylabel("Average")
		plt.show
        
		canvas = FigureCanvasTkAgg(fig, master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)

		
	

class Graph2:
	def __init__(self, root, number):
		
		bins = 20
		iris = datasets.load_iris()
		X_iris = iris.data
		fig2, axs = plt.subplots(2, 2)
		axs[0, 0].hist(X_iris[:, 0])
		axs[0, 1].hist(X_iris[:, 1], color='orange')
		axs[1, 0].hist(X_iris[:, 2], color='green')
		axs[1, 1].hist(X_iris[:, 3], color='red')

		i = 0
		for ax in axs.flat:
			ax.set(xlabel=iris.feature_names[i], ylabel='Frequency')
			i += 1

		fig2.suptitle("2- Iris Histograms")
		
		canvas = FigureCanvasTkAgg(fig2, master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()
		

		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)
		
	
class Graph3:
	def __init__(self, root, number):
		
		
		iris = datasets.load_iris()
		# The indices of the features that we are plotting
		x_index = 0
		y_index = 1

		# this formatter will label the colorbar with the correct target names
		formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

		fig3 = plt.figure(figsize=(5, 4))
		fig3.suptitle("3- Plot 2D Views of the Dataset")
		plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
		plt.colorbar(ticks=[0, 1, 2], format=formatter)
		plt.xlabel(iris.feature_names[x_index])
		plt.ylabel(iris.feature_names[y_index])

		
		canvas = FigureCanvasTkAgg(fig3, master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()
		

		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)

class Graph4:
	def __init__(self, root, number):
		
		fig4 = plt.figure()
		fig4.suptitle("4- Bar Chart Setosa Averages")
		iris = datasets.load_iris()
		X_iris = iris.data
		Y_iris = iris.target
		
		average = X_iris[Y_iris == 0].mean(axis=0)

		plt.bar(iris.feature_names, average)
		plt.ylabel("Average (in cm)")
	
		canvas = FigureCanvasTkAgg(fig4, master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)
		
	

class Graph5:
	def __init__(self, root, number):
		
		iris = datasets.load_iris()  # load dataset
		X_iris = iris.data[:, :2]  # only take the first two features
		Y_iris = iris.target
		fig5= plt.figure()
		fig5.suptitle("5- Scatter Plot")
		n_classes = 3
		for i in range(n_classes):
			index = np.where(Y_iris == i)
			plt.scatter(X_iris[index, 0], X_iris[index, 1],  
			label=iris.target_names[i])
		
		plt.legend()
		plt.xlabel(iris.feature_names[0])
		plt.ylabel(iris.feature_names[1])
		plt.show
	
		canvas = FigureCanvasTkAgg(fig5,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)
		
	

class Graph6:
	def __init__(self, root, number):
		
		bins = 20
		iris = datasets.load_iris()
		X_iris = iris.data
		X_sepal = X_iris[:, 0]
		fig6 = plt.figure()
		plt.hist(X_sepal, bins)
		plt.title("6- Histogram Sepal Length")
		plt.xlabel(iris.feature_names[0])
		plt.ylabel("Frequency")
		plt.show
	
		canvas = FigureCanvasTkAgg(fig6,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)
		
	

class Graph7:
	def __init__(self, root, number):
		
		# import some data to play with
		iris = datasets.load_iris()
		y = iris.target
		# To getter a better understanding of interaction of the dimensions
		# plot the first three PCA dimensions
		fig7 = plt.figure(figsize=(8, 6))
		fig7.suptitle("7- First three PCA directions")
		ax = Axes3D(fig7, elev=-150, azim=110)
		X_reduced = PCA(n_components=3).fit_transform(iris.data)
		ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
				cmap=plt.cm.Set1, edgecolor='k', s=40)
		ax.set_xlabel("1st eigenvector")
		ax.w_xaxis.set_ticklabels([])
		ax.set_ylabel("2nd eigenvector")
		ax.w_yaxis.set_ticklabels([])
		ax.set_zlabel("3rd eigenvector")
		ax.w_zaxis.set_ticklabels([])

		canvas = FigureCanvasTkAgg(fig7,master=root)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)
		
class Graph8:
	def __init__(self, root, number):
		
		iris = datasets.load_iris()
		X_iris = iris.data
		X_sepal = X_iris[:, 0]
		fig8 = plt.figure()
		plt.boxplot(X_sepal, labels=[iris.feature_names[0]])
		plt.title("8- Boxplot Sepal Length")
		plt.ylabel("cm")
		plt.show


		canvas = FigureCanvasTkAgg(fig8,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)


class Graph9:
	def __init__(self, root, number):
		
		iris = datasets.load_iris()
		X_iris = iris.data
		fig9 = plt.figure()
		plt.boxplot(X_iris, labels=[iris.feature_names[0], iris.feature_names[1], iris.feature_names[2], iris.feature_names[3]])
		plt.title("9- Boxplots Iris features")
		plt.ylabel("cm")
		plt.show


		canvas = FigureCanvasTkAgg(fig9,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)	

class Graph10 :
	def __init__(self, root, number):
		
		iris = datasets.load_iris() # load the iris dataset
		# print("Keys:", iris.keys()) # print keys of dataset

		# # shape of data and target
		# print("Data shape", iris.data.shape) # (150, 4)
		# print("Target shape", iris.target.shape) # (150,)

		# print("data:", iris.data[:4]) # first 4 elements

		# # unique targets
		# print("Unique targets:", np.unique(iris.target)) # [0, 1, 2]
		# # counts of each target
		# print("Bin counts for targets:", np.bincount(iris.target))

		# print("Feature names:", iris.feature_names)
		# print("Target names:", iris.target_names)

		colors = ['blue', 'red', 'green']
		# plot histogram
		fig10=plt.figure()
		for feature in range(iris.data.shape[1]): # (shape = 150, 4)
			
			plt.subplot(2, 2, feature+1) # subplot starts from 1 (not 0)
			for label, color in zip(range(len(iris.target_names)), colors):
				# find the label and plot the corresponding data
				plt.hist(iris.data[iris.target==label, feature],
						label=iris.target_names[label],
						color=color)
			plt.xlabel(iris.feature_names[feature])
			plt.legend()


		canvas = FigureCanvasTkAgg(fig10,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)		

class Graph11 :
	def __init__(self, root, number):
		
		iris = datasets.load_iris() # load the iris dataset
		# print("Keys:", iris.keys()) # print keys of dataset

		# # shape of data and target
		# print("Data shape", iris.data.shape) # (150, 4)
		# print("Target shape", iris.target.shape) # (150,)

		# print("data:", iris.data[:4]) # first 4 elements

		# # unique targets
		# print("Unique targets:", np.unique(iris.target)) # [0, 1, 2]
		# # counts of each target
		# print("Bin counts for targets:", np.bincount(iris.target))

		# print("Feature names:", iris.feature_names)
		# print("Target names:", iris.target_names)

		colors = ['blue', 'red', 'green']
		fig11=plt.figure()
		# # plot histogram
		# for feature in range(iris.data.shape[1]): # (shape = 150, 4)
			# plt.subplot(2, 2, feature+1) # subplot starts from 1 (not 0)
			# for label, color in zip(range(len(iris.target_names)), colors):
				# # find the label and plot the corresponding data
				# plt.hist(iris.data[iris.target==label, feature],
						# label=iris.target_names[label],
						# color=color)
			# plt.xlabel(iris.feature_names[feature])
			# plt.legend()

		# plot scatter plot : petal-width vs all features
		feature_x= 3 # petal width
		for feature_y in range(iris.data.shape[1]):
			plt.subplot(2, 2, feature_y+1) # subplot starts from 1 (not 0)
			for label, color in zip(range(len(iris.target_names)), colors):
				# find the label and plot the corresponding data
				plt.scatter(iris.data[iris.target==label, feature_x],
							iris.data[iris.target==label, feature_y],
							label=iris.target_names[label],
							alpha = 0.45, # transparency
							color=color)
			plt.xlabel(iris.feature_names[feature_x])
			plt.ylabel(iris.feature_names[feature_y])
			plt.legend()


		canvas = FigureCanvasTkAgg(fig11,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)		

class Graph12 :
	def __init__(self, root, number):
		
		iris = datasets.load_iris()

		fig12, ax = plt.subplots()
		x_index = 3
		colors = ['blue', 'red', 'green']

		for label, color in zip(range(len(iris.target_names)), colors):
			ax.hist(iris.data[iris.target==label, x_index], 
					label=iris.target_names[label],
					color=color)

		ax.set_xlabel(iris.feature_names[x_index])
		ax.legend(loc='upper right')

		canvas = FigureCanvasTkAgg(fig12,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)		


class Graph13 :
	def __init__(self, root, number):
		
		iris = datasets.load_iris()

		fig13, ax = plt.subplots()

		x_index = 3
		y_index = 0

		colors = ['blue', 'red', 'green']

		for label, color in zip(range(len(iris.target_names)), colors):
			ax.scatter(iris.data[iris.target==label, x_index], 
						iris.data[iris.target==label, y_index],
						label=iris.target_names[label],
						c=color)

		ax.set_xlabel(iris.feature_names[x_index])
		ax.set_ylabel(iris.feature_names[y_index])
		ax.legend(loc='upper left')

		canvas = FigureCanvasTkAgg(fig13,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)		

class Graph14 :
	def __init__(self, root, number):
		
		iris = datasets.load_iris()

		n = len(iris.feature_names)
		fig14, ax = plt.subplots(n, n, figsize=(8, 8))

		colors = ['blue', 'red', 'green']

		for x in range(n):
			for y in range(n):
				xname = iris.feature_names[x]
				yname = iris.feature_names[y]
				for color_ind in range(len(iris.target_names)):
					ax[x, y].scatter(iris.data[iris.target==color_ind, x], 
									iris.data[iris.target==color_ind, y],
									label=iris.target_names[color_ind],
									c=colors[color_ind])

				ax[x, y].set_xlabel(xname)
				ax[x, y].set_ylabel(yname)
				ax[x, y].legend(loc='upper left')
		canvas = FigureCanvasTkAgg(fig14,master=root) 
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()


		def on_key_press(event):
			print("you pressed {}".format(event.key))
			key_press_handler(event, canvas, toolbar)


		canvas.mpl_connect("key_press_event", on_key_press)	

root = tk.Tk()
root.configure(background='#2d2d4c')
app = Main(root)
root.mainloop()