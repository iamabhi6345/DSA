// node  
// data , left , right


node *findlca(node * root , int a , int b)
{
    if(!root) return nullptr;
    if(root->data > a && root->data > b)
    {
        return findlca(root->left , a , b);
    }
    if (root->data < a && root->data < b)
    {
        return findlca(root->right , a , b);
    }
    return root;
}

int finddistancefromroot(node * root , int key)
{
    // key 22      root 22 dist 1
    if (root->data == key) return 0;
    if (root->data > key)return 1+ finddistancefromroot(root->left , key);
    else return 1+ finddistancefromroot(root->right , key);
}

int finddistancebetweennode(node *root , int a , int b)
{
    node * lca = findlca(node *root , int a , int b);
    ind d1 = finddistancefromroot(lca , a);
    int d2=finddistancefromroot(lca , b);
    return d1+d2;
}