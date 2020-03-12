// Jonpierre Grajales
// Professor Rengesh
// CS 435
// Project 1 - Part 1

import java.util.*;
import java.io.*;

class Node 
{ 
    int key; 
    Node left, right; 
  
    public Node(int item) 
    { 
        key = item; 
        left = right = null; 
    } 
} 
  
class BinaryTree 
{ 
    Node root; 
    ArrayList list = new ArrayList();

    BinaryTree() 
    { 
        root = null; 
    } 

    void print()
    {
      for(int i = 0; i < list.size(); i++) 
      {   
        System.out.print(list.get(i));
      }  
    }

    void sort(Node node) 
    { 
        if (node == null) 
            return; 
  
        // left
        sort(node.left); 
  
        // visit
        list.add(node.key + " ");
  
        // right
        sort(node.right); 
    } 
  
    void sort()    
    {     
      sort(root);   
    } 
}

class Main
{
    public static void main(String[] args) 
    { 
        // using values from 2A
        BinaryTree tree = new BinaryTree(); 
        tree.root = new Node(10); 
        tree.root.left = new Node(5);
        tree.root.right = new Node(20); 
        tree.root.left.right = new Node(6); 
        tree.root.right.left = new Node(12);
        tree.root.left.right.right = new Node(7); 
        tree.root.right.left.left = new Node(11);
        tree.root.right.left.right = new Node(16);
        tree.root.right.left.right.right = new Node(19);
        tree.root.right.left.right.right.left = new Node(18);
        tree.root.right.left.right.right.left.left = new Node(17);

        
        tree.sort(); 
        System.out.println("\nSorted elements:  "); 
        tree.print();
    } 
}
