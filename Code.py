"""
Code for calculation of different distances between the
conjugate points of an imaging system

Group members:
    Juan Fernando Riascos Goyes
    Thomas Martinod Saldarriaga
    Amelia Hoyos Velez
"""


def calcular_sistema_lentes(dObj=None, dImg=None, M=None, f=None, calcular=None):
    """
    Function to calculate different variables in an imaging system.
    
    Parameters:
    - dObj: Object distance (in mm)
    - dImg: Image distance (in mm)
    - M: Magnification
    - f: Focal length (in mm)
    - The variable to calculate (given by user) ('dObj', 'dImg', 'M', 'f')
    
    Returns:
    - The calculated value with two decimal points, or an error message if the input is insufficient or invalid syntaxis.
    """
 
    # Case 1: Calculate the image distance (dImg)
    if calcular == 'dImg':
        if f is not None and dObj is not None:
            # Using the lens equation: 1/f = 1/dObj + 1/dImg [Eq. (1) on paper]
            dImg = 1 / ((1/f) - (1/dObj))
            return f"dImg = {dImg:.2f} mm"
        elif M is not None and dObj is not None:
            # Using the magnification equation: M = -dImg/dObj [Eq. (3) on paper]
            dImg = -M * dObj
            return f"dImg = {dImg:.2f} mm"
    
    # Case 2: Calculate the object distance (dObj)
    elif calcular == 'dObj':
        if f is not None and dImg is not None:
            # Using the lens equation: 1/f = 1/dObj + 1/dImg [Eq. (1) on paper]
            dObj = 1 / ((1/f) - (1/dImg))
            return f"dObj = {dObj:.2f} mm"
        elif M is not None and dImg is not None:
            # Using the magnification equation: M = -dImg/dObj [Eq. (3) on paper]
            dObj = -dImg / M
            return f"dObj = {dObj:.2f} mm"
    
    # Case 3: Calculate the focal length (f)
    elif calcular == 'f':
        if dObj is not None and dImg is not None:
            # Using the lens equation: 1/f = 1/dObj + 1/dImg [Eq. (1) on paper]
            f = 1 / ((1/dObj) + (1/dImg))
            return f"f = {f:.2f} mm"
    
    # Case 4: Calculate the magnification (M)
    elif calcular == 'M':
        if dObj is not None and dImg is not None:
            # Using the magnification equation: M = -dImg/dObj [Eq. (3) on paper]
            M = -dImg / dObj
            return f"M = {M:.2f}"
    
    # If not enough information is provided or invalid syntaxis of data
    return "Insufficient data or invalid combination."

# Function to prompt user for input and calculate the desired variable output
def user_input():
    print("Welcome to the lens system calculator. Please input the following values, or press Enter to skip a value.")

    # Get user inputs for the variables
    dObj = input("Enter the object distance (dObj) in mm, or leave blank if unknown: ")
    dImg = input("Enter the image distance (dImg) in mm, or leave blank if unknown: ")
    M = input("Enter the magnification (M), or leave blank if unknown: ")
    f = input("Enter the focal length (f) in mm, or leave blank if unknown: ")
    calcular = input("What would you like to calculate? ('dObj', 'dImg', 'M', 'f'): ")

    # Convert the inputs to floats if they are provided
    dObj = float(dObj) if dObj else None
    dImg = float(dImg) if dImg else None
    M = float(M) if M else None
    f = float(f) if f else None

    # Call the function with user inputs
    result = calcular_sistema_lentes(dObj=dObj, dImg=dImg, M=M, f=f, calcular=calcular)
    
    # Display the result
    print(result)

# Run the user input function to allow interaction
user_input()

