
#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>

int main()
{
   int n;
   scanf("%d",&n);
   int arr[n];
   for (int i=0 ; i<n ;i++)
   {
    scanf("%d",&arr[i]);
   }
   int i=0;
   while(i<n-1)
   {
        int j=i+1;
        bool check =true;

        while(j<n && arr[j]==arr[i] )
        {   
            if(check)
            {
                      printf("%d  ",arr[i]);
                       check =false;
            }
            j=j+1;
        }
        i = i+1;
   }
    return 0;
}