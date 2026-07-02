##A reusable explore(df) function that takes any DataFrame, auto-detects column types, shows stats, distributions, correlations, and generates visual charts. This is a basic one
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def plot_graph(df):
    if df is None or df.empty:
        print("No data available.")
        return

    print("\nGraphs\n1.Line Graph\n2.Pie Chart\n")
    command = input("Select a graph: ")

    match command:
        case "1":
            print("Print multiple line graphs. Enter 'plot' to quit.")
            plt.figure()

            while True:
                command = input("Select a option for line graph > 'new' or 'plot': ")
                if command == "new":
                    x_col = input("Enter x column: ")
                    y_col = input("Enter y column: ")
                    label_text = input("Select legend text: ")
                    sorted_df = df.sort_values(x_col)
                    plt.plot(sorted_df[x_col],sorted_df[y_col],linestyle = "-",marker = "o",label = label_text)
                    plt.legend()
                    plt.grid(True)
                    continue
                elif command == "plot":
                    plt.show(block= False)
                    plt.pause(0.2)
                    plt.figure()
                    return
                else:
                    print("Invalid option.")
                    continue
        
        case "2":
            x_col = input("Enter group by column: ")
            y_col = input("Enter the name of column to find count: ")
            grouped_df = df.groupby(x_col)[y_col].count()
            plt.pie(grouped_df.values,labels=grouped_df.index,autopct="%1.1f%%")
            plt.grid(True)
            plt.show(block = False)
            plt.pause(0.2)
            plt.figure()

        case "4":
            print("Invalid option")

def get_data(file_path):
     # get data
    if not file_path:
        print("Enter correct file path a file path")
        return None

    df = pd.read_csv(file_path)
    print("\n*****Info of the file*******\n")
    print(df.info())
    print("\nStatistical summary\n")
    print(df.describe())
    print("\nFirst few rows\n")
    print(df.head())
    print("\nColumns of the data\n")
    print(list(df.columns))
    return df
        


def data_explorer():
    print("This is a Data explorer!.")
    df = None
    file_path = None

    while True:
        print("\nMenu\n1.Enter file path\n2.Get File Info\n3.Plot graphs\n4.Exit\n")
        user_input = input("\nDataExplorer > ").strip()

        match user_input:
            case "1":
                file_path = Path(input("Enter file path: "))
                if not file_path.exists():
                    print("File path does not exists. Enter valid file path.")
                    file_path = None
                    continue
                else : 
                    print("File found")

            case "2":
                df = get_data(file_path)

            case "3":
                plot_graph(df)

            case "4":
                break

            case _:
                print("This option does not exist.")
                continue
            

if __name__ == "__main__":
    data_explorer()