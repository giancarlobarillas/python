#This program opens a text file and reads the data.
#It then displays the data in a line graph
import matplotlib.pyplot as plt
def main():
    #open text file and store data in list
    text_file=open("1994_Weekly_Gas_Averages.txt","r")
    data = [float(line[:-1]) for line in text_file]
    text_file.close()
    #customize the plot to have a line graph of the data
    #line graph will have labeled axis and title
    plt.plot(data)
    plt.title("1994 Weekly Gas Averages")
    plt.xlabel("Intervals")
    plt.ylabel("Gas Averages")
    plt.show()

main()
