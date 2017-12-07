#include "lists.h"

/**
 *check_cycle - checks if circular list
 *@list: list
 *Return: 0 or 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	//same struct for both fast and slow
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
		return (0);

	//check if fast's next and next are NULL
	while (fast->next != NULL && fast->next->next != NULL)
	{
		//move slow by one
		slow = slow->next;
		//move fast by two
		flast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
