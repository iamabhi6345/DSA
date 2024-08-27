#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int new_data)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = NULL;
    return new_node;
}

// Function to insert a new node at the beginning of the list
struct Node* insertAtFront(struct Node* head, int new_data)
{
    struct Node* new_node = createNode(new_data);
    new_node->next = head;
    return new_node;
}

// Function to insert a new node at the end of the list
struct Node* insertAtEnd(struct Node* head, int new_data)
{
    struct Node* new_node = createNode(new_data);

    if (head == NULL) {
        return new_node;
    }

    struct Node* curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
    }

    curr->next = new_node;
    return head;
}

// Function to insert a new node after a specific value
struct Node* insertAfterValue(struct Node* head, int value, int new_data)
{
    struct Node* curr = head;

    while (curr != NULL && curr->data != value) {
        curr = curr->next;
    }

    if (curr != NULL) {
        struct Node* new_node = createNode(new_data);
        new_node->next = curr->next;
        curr->next = new_node;
    }

    return head;
}

// Function to delete a node at the beginning of the list
struct Node* deleteAtFront(struct Node* head)
{
    if (head == NULL) {
        return NULL;
    }
    
    struct Node* temp = head;
    head = head->next;
    free(temp);
    
    return head;
}

// Function to delete a node at the end of the list
struct Node* deleteAtEnd(struct Node* head)
{
    if (head == NULL) {
        return NULL;
    }
    
    if (head->next == NULL) {
        free(head);
        return NULL;
    }
    
    struct Node* curr = head;
    while (curr->next->next != NULL) {
        curr = curr->next;
    }
    
    free(curr->next);
    curr->next = NULL;
    
    return head;
}

// Function to delete a node with a specific value
struct Node* deleteByValue(struct Node* head, int value)
{
    if (head == NULL) {
        return NULL;
    }

    if (head->data == value) {
        struct Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    struct Node* curr = head;
    while (curr->next != NULL && curr->next->data != value) {
        curr = curr->next;
    }

    if (curr->next != NULL) {
        struct Node* temp = curr->next;
        curr->next = curr->next->next;
        free(temp);
    }

    return head;
}

void printList(struct Node* head)
{
    struct Node* curr = head;
    while (curr != NULL) {
        printf(" %d", curr->data);
        curr = curr->next;
    }
    printf("\n");
}

int main()
{
    // Create the linked list 2->3->4->5
    struct Node* head = createNode(2);
    head->next = createNode(3);
    head->next->next = createNode(4);
    head->next->next->next = createNode(5);

    // Print the original list
    printf("Original Linked List:");
    printList(head);

    // Insert a new node at the front of the list
    printf("After inserting 1 at the front:");
    head = insertAtFront(head, 1);
    printList(head);

    // Insert a new node at the end of the list
    printf("After inserting 6 at the end:");
    head = insertAtEnd(head, 6);
    printList(head);

    // Insert a new node after a specific value
    printf("After inserting 7 after 4:");
    head = insertAfterValue(head, 4, 7);
    printList(head);

    // Delete a node at the front of the list
    printf("After deleting at the front:");
    head = deleteAtFront(head);
    printList(head);

    // Delete a node at the end of the list
    printf("After deleting at the end:");
    head = deleteAtEnd(head);
    printList(head);

    // Delete a node with a specific value
    printf("After deleting the node with value 4:");
    head = deleteByValue(head, 4);
    printList(head);

    return 0;
}
