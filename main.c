#include <stdio.h>
#include <stdlib.h>
#include<time.h>
unsigned short l, u;

typedef struct {
    double sum;
    unsigned short st, dr, dim;
}deq;

unsigned char hasPosSubArr(unsigned short n, unsigned short data[2][n],
        double cat){
    double diff[n];
    unsigned short i;
    deq mainDEQ, auxDEQ;
    mainDEQ.sum = 0;
    l--;
    //The main deque is initialised.
    for( i  = 0 ; i < l ; i++ ){
        diff[i] = data[0][i]-cat*data[1][i];
        mainDEQ.sum += diff[i];
    }
    for( i = l ; i < n ; i++ )
        diff[i] = data[0][i]-cat*data[1][i];
    l++;

    mainDEQ.st = 0;
    mainDEQ.dr = l - 2;
    mainDEQ.dim = l - 1;
    auxDEQ.sum = auxDEQ.dim = 0;
    for( i = l - 1 ; i < n ; i++ ){
        if( mainDEQ.sum + diff[i] >= 0 )
            return 1;

        mainDEQ.sum += diff[i];
        mainDEQ.dim ++;
        mainDEQ.dr ++;

        //The prefix deque is enlarged.
        if( auxDEQ.dim > 0 ){
            auxDEQ.dr ++;
            auxDEQ.sum += diff[auxDEQ.dr];
        } else {
            auxDEQ.dr = auxDEQ.st = mainDEQ.st;
            auxDEQ.sum += diff[mainDEQ.st];
        }
        auxDEQ.dim ++;

        if(mainDEQ.dim > u - 1){
            mainDEQ.sum -= diff[mainDEQ.st];
            mainDEQ.st ++;
            mainDEQ.dim --;

            auxDEQ.sum -= diff[auxDEQ.st];
            auxDEQ.st ++;
            auxDEQ.dim --;
        }

        //The prefix deque is erased if its sum is negative.
        if( auxDEQ.sum <= 0 && auxDEQ.dim > 0 ){
            mainDEQ.sum -= auxDEQ.sum;
            mainDEQ.st = auxDEQ.dr + 1;
            mainDEQ.dim -= auxDEQ.dim;

            auxDEQ.sum = auxDEQ.dim = 0;
        }
    }

    return 0;
}

void main(){
    FILE * fi = fopen("secv3.in","rt");
    unsigned short n, i;
    fscanf( fi , "%hd %hd %hd\n" , &n , &l , &u );
    unsigned short data[2][n];
    n--;
    for(i = 0 ; i < n ; i++ )
        fscanf( fi , "%hd " , &data[0][i] );
    fscanf( fi , "%hd\n" , &data[0][n] );
    for(i = 0 ; i < n ; i++ )
        fscanf( fi , "%hd " , &data[1][i] );
    fscanf( fi , "%hd" , &data[1][n] );
    n++;
    fclose(fi);

    //The approximation
    double ans = 0, j;
    for( j = 1 << 10 ; j > 0.000001 ; j /= 2 )
        if( hasPosSubArr( n, data, j + ans ) )
            ans+=j;

    fi = fopen("secv3.out","wt");
    fprintf(fi,"%.2f\n", ans);
    fclose(fi);
}
