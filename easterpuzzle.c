/*  Easter Egg Puzzle 
    Solving dimensions x,y,z (x>y>z>0)
*/

#include <stdio.h>

int main() {
    int x,y,z;
    while(z>0 && y>z && x>y){
        if (4*z^3==x*y^2){
            printf("x= %d mm\n",x);
            printf("y= %d mm\n",y);
            printf("z= %d mm\n",z);
        }
        else {
            printf("No solution\n");
        }
    }
    return 0;
}
