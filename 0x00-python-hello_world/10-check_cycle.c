include "lists.h"

/**
* check_cycle - check if listint_t have loop
* @list: list of int
*
* Return: 1 if have loop | 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *t = list;
	listint_t *r = list;

	while ((r && r->next) && t)
	{
		t = (*t).next;
		r = (*r).next->next;
		if (t == r)
			return (1);
	}
	return (0);
}
