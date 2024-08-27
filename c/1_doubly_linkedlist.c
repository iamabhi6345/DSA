#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

struct Node* createNode(int new_data)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = NULL;
    new_node->prev = NULL;
    return new_node;
}

// Function to insert a new node at the beginning of the list
struct Node* insertAtFront(struct Node* head, int new_data)
{
    struct Node* new_node = createNode(new_data);
    if (head != NULL) {
        head->prev = new_node;
    }
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
    new_node->prev = curr;
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
        new_node->prev = curr;

        if (curr->next != NULL) {
            curr->next->prev = new_node;
        }
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

    if (head != NULL) {
        head->prev = NULL;
    }

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
    while (curr->next != NULL) {
        curr = curr->next;
    }

    curr->prev->next = NULL;
    free(curr);
    return head;
}

// Function to delete a node with a specific value
struct Node* deleteByValue(struct Node* head, int value)
{
    if (head == NULL) {
        return NULL;
    }

    struct Node* curr = head;

    while (curr != NULL && curr->data != value) {
        curr = curr->next;
    }

    if (curr != NULL) {
        if (curr->prev != NULL) {
            curr->prev->next = curr->next;
        } else {
            head = curr->next;
        }

        if (curr->next != NULL) {
            curr->next->prev = curr->prev;
        }

        free(curr);
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
    // Create the doubly linked list 2<->3<->4<->5
    struct Node* head = createNode(2);
    head->next = createNode(3);
    head->next->prev = head;
    head->next->next = createNode(4);
    head->next->next->prev = head->next;
    head->next->next->next = createNode(5);
    head->next->next->next->prev = head->next->next;

    // Print the original list
    printf("Original Doubly Linked List:");
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
