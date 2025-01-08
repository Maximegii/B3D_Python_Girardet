import matplotlib.pyplot as plt
import numpy as np

## histogramme
# data = np.random.randn(1000)
# plt.hist(data)
# plt.show()


## courbe
# x = [1, 2, 3, 4, 5]
# y = [10, 8, 6, 4, 2]
# plt.bar(x, y)
# plt.show()


# # nuage de points
# x = np.random.randn(100)
# y = 2 * x + np.random.randn(100)
# plt.scatter(x, y)
# plt.show()


# ## graphique 3D
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x = np.random.randn(100)
# y = np.random.randn(100)
# z = np.random.randn(100)
# ax.scatter(x, y, z)
# plt.show()

nyc_temp_2005 = [25.9, 30.3, 30.4, 27.4, 35.5, 36.8, 28.8, 31.0, 32.0, 35.3, 34.0, 36.4]
nyc_temp_2010 = [30.3, 21.3, 22.2, 27.0, 25.5, 20.3, 19.3, 32.7, 29.0, 26.0, 25.3, 25.1]
nyc_temp_2015 = [40.3, 41.3, 38.2, 39.0, 20.9, 21.3, 20.3, 35.6, 38.0, 37.0, 32.1, 31.0]
months = range(1, 13)
plt.plot(
		months, nyc_temp_2005, 
        months, nyc_temp_2010, 
        months, nyc_temp_2015
    )
plt.legend([2005, 2010, 2015], loc='upper left')
plt.title('temperature NYC')
plt.xlabel('Mois')
plt.ylabel('Temperature')
plt.show()

import os
rep_courant = os.path.abspath(os.path.dirname(__file__))
chemin_fichier = os.path.join(rep_courant, "graphique.jpg")
plt.savefig(chemin_fichier)