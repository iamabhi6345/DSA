#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>
int compare(const void *a , const void *b)
{
    return (  *(int*)a  - *(int*)b     );
}
int main()
{
   int n;
   scanf("%d",&n);
   int arr[n];
   for (int i=0 ; i<n ;i++)
   {
    scanf("%d",&arr[i]);
   }
   qsort(arr , n, sizeof(int) ,  compare );
   int i=0;
   while(i<n)
   {
        int j=i+1;
        bool check =true;
        while(j<n && arr[j]==arr[i] )
        {   
            check =false;
            j=j+1;
        }
        if (check == true)
        {
            printf("%d  ",arr[i]);
        }
        i = j;
   }
    return 0;
}


