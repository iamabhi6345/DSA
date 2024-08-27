#include<stdio.h>
#include<stdlib.h>

int compare(const void *a , const void *b)
{
    return (  *(int*)a  - *(int*)b     );
}

void main()
{
    int arr[]={5,3,4,5,1,23,3,89,-87};
    size_t n= sizeof(arr)/sizeof(arr[0]);

    qsort(arr , n, sizeof(int) ,  compare );
    for(int i=0; i<n;i++)
    {
        printf("%d ", arr[i]);
    }

}