#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *current = list;

	while (current != NULL)
	{
		if (head == (current->next))
			return (1);
		current = current->next;
	}
	return (0);
}
