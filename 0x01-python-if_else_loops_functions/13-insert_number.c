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
	listint_t *c_n;

	if (n_n == NULL)
		return (NULL);
	(*n_n).n = number;

	if (*head == NULL)
	{
		*head = n_n;
		(*n_n).next = NULL;
		return (n_n);
	}
	c_n = *head;
	while (c_n != NULL)
	{
		if (number <= c_n->n)
		{
			n_n->next = c_n;
			*head = n_n;
			return (n_n);
		}
		if ((number >= c_n->n) && (c_n->next == NULL))
		{
			n_n->next = NULL;
			c_n->next = n_n;
			return (n_n);

		}

		if ((number >= c_n->n) && (number <= c_n->next->n))
		{
			(*n_n).next = c_n->next;
			(*c_n).next = n_n;
			return (n_n);
		}
		c_n = c_n->next;
	}
	return (NULL);
}
