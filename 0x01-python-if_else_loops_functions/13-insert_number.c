#include "lists.h"

/**
* insert_node - add int in sorted linked list
* @head: start of node
* @number: int
*
* Return: node | NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_n = malloc(sizeof(listint_t));
	listint_t *c_n = *head;
	listint_t *nxt_n = c_n->next;

	if (head == NULL)
		return (NULL);
	(*n_n).n = number;
	if (*head == NULL)
	{
		*head = n_n;
	}
	if ((*c_n).n > number)
	{
		(*n_n).next = *head;
		*head = n_n;
	}
	while (nxt_n != NULL)
	{
		if (number > (*nxt_n).n)
		{
			nxt_n = (*nxt_n).next;
			c_n = (*c_n).next;
		}
		else
			break;
	}
	(*c_n).next = n_n;
	(*n_n).next = nxt_n;
	return (n_n);
}
