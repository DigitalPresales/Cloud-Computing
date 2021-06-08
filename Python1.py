
import os
def main(name):
    print(f'Hi, {name}')
    x, y = 5, 9

    if (x < y):
        print("%i is less than %i" %(x,y) )
if __name__ == '__main__':    // is used to execute some code only if the file was run directly, and not imported.
    main('Digital PreSales')
    
# If you import this script as a module in another script, the __name__ is set to the name of the script/module.
# So basically it either acts as a reusable modules, or as standalone programs. 
