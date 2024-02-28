#include <stdio.h>

int top = 3;
int n = 10;
int stack[5] = {1, 2, 3, 4};

void pop() 
{
    if(top == -1)
        printf("Underflow\n");
    else 
        top--;
}

void push(int a)
{
    if(top == 9)
        printf("Oveflow!\n");
    else
    {
        stack[top] = a;
        top++;
    }
}

void display() 
{
    if(top == -1)
        printf("Underflow\n");
    else 
    {
        for(int i = 0; i < top; i++)
            printf("%d\t", stack[i]);
    }
    printf("\n");
}

void main()
{
    push(5);
    push(11);
    push(12);
    pop();
    push(10);
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();
    for(int i = 0; i < n; i++)
    pop();
}