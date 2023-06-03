import pandas as pd
import plotly.graph_objects as go
from helperfunc.helper import helper_function1, helper_function2, two_sum
from helperfunc.leetcode import Solution


def main():
    print("Welcome to My Project!")
    helper_function1()
    helper_function2()

    nums = [3, 7, 11, 15]
    #target = 14
    target = int(input("Enter the target value: "))
    result = two_sum(nums, target)
    print(result)

    leetcode_sol = Solution()
    result = leetcode_sol.twoSum(nums, target)
    print(f'Result from Object : {result}')  

    print(f'Reverse of Target : {leetcode_sol.reverse(target)}')

    print(leetcode_sol.isValid('welcome class of 20 (2020)'))
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 2, 3, 4, 5]
    # Create a new plot for each iteration
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name=f'Plot {1}'))
    fig.show()


if __name__ == "__main__":
    main()
