# Julia-Set-Generator
A Python program that displays the mandelbrot family of Julia Sets. Created by Sara Birkby as the final project for the University of Nebraska at Omaha CSCI 1620 course.


Help Menu:
  
(1) The coefficient entry decides the coefficients and degree of the polynomial used in the recursive function. ex. 1,2,3,0 => zₙ₊₁ = 1×zₙ³ + 2×zₙ² + 3×zₙ + 0
    The length of the input determines the degree of the polynomial. 
  
  
  
On Imaginary & Complex Numbers:
  New math is discovered, more often than not, by assuming something exists and through its consequences determine its validity. The square roots of certain numbers—
  2 and 3 for instance—prove to be too difficult to fully calculate. Though these numbers are troublesome, their values undoubtedly fall on the real number line.
  But what about the square root of negative numbers? Some have chosen to write this off as simply a problem without a solution. I believe (as do many mathematicians 
  before me) that it is more useful to instead define a number who simply has the property that is square is equal to negative one. Such a number surly cannot be found
  on the real number line, so a new line perpendicular to the real axis was added, making up what is known as the complex plane. These new 'imaginary' numbers—
  despite their unfortunate name—are quite real. They describe many real world phenomena that don't follow simple rules, especially those involving oscillation such as
  electrical systems, quantum mechanics, and even the motion of springs. 
  
About These Sets:
  This program relies on the strange arithmetic properties of complex numbers. The famous Mandelbrot set, the inspiration and basis for this program is displayed
by associating each pixel with a complex number over a certain range, with the pixel's horizontal position determining its real value, and the vertical: its imaginary. 
Each pixel's value 'c' is then calculated in the function: zₙ₊₁ = zₙ² + c, where n goes from 0 to the desired number of iterations. The initial z value is 0,
and each pixel whose 'c' value does *not* continue growing to infinity is part of the set and colored black. The other pixels, those who reach the threshold value
(by default 2), are colored based on how many iterations it took to reach it. The points very close to the set will require more iterations to reach the threshold value
and if not given a high enough value, the displayed set will include pixels that are not actually part of the set, simply those who didn't have enough iterations to reach
the threshold. 

