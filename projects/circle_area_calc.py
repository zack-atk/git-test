
# -------------------------------------------------
#             CALCULATE THE AREA OF A CIRCLE
# -------------------------------------------------
# radius = input('Enter the radius of your circle (m):')
# area = 3.142 * int(radius) ** 2
# print('The area of your cirlce is:', area)
# -------------------------------------------------
#                  USING A FUNCTION
#------------------------------------------------------
# def area(radius):
#     print('The area is:', 3.142 * radius ** 2, units)

# radius = int(input('Enter the radius -> '))
# units = input('enter the unit of measurement -> ')

# area(radius)
# ------------------------------------------------------
#          CALCULATE THE VOLUME OF A CYLINDER
# ------------------------------------------------------
# THE 'RETURN' KEYWORD CAN BE USED TO PASS A FUNTION RESULT INTO ANOTHER FUNCTION
# -------------------------------------------------------
def area(radius):
    return 3.142 * radius ** 2  # USING RETURN

def vol(area,length):
    print('The volume is:', area * length, 'cubic', units)

radius = int(input('Enter the radius -> '))
length = int(input('Enter the length -> '))
units = input('enter the unit of measurement -> ')
 
vol(area(radius),length) 