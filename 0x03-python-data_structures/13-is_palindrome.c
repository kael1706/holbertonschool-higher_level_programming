#include "lists.h"

/**
* is_palindrome - check if is palindrome
* @head: start of linked list
* Return: 0 | 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	listint_t *end = *head;
	unsigned int c1 = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL || start->next == NULL)
		return (1);
	while (start && end->next)
	{
		if (start->next == end || start == end)
			return (1);
		end = (*end).next;
		if (start->n != end->n)
			return (0);
		start = (*start).next;
		c1++;
	}
	return (0);
}
