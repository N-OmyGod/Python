from matplotlib import colors
import matplotlib.pyplot as plt

bags = ["Tamaris", "Gucci", "Dior", "Saint-Laurent", "Chanel"]
prices = [6000, 80000, 20000, 70000, 170000]
plt.bar(bags, prices, color="purple")
plt.title("Bags!")
plt.xlabel("Bag")
plt.ylabel("price")
plt.show()
