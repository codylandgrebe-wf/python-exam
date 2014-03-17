class ShoppingList():
    def __init__(self, items):
        self.items = items

    def show_list(self):
        """
        @summary: Prints ShoppingList with borders and space formatting. The
        width of list is determined by the longest item in the list.
        Example:
        My Shopping List:       My Shopping List:
        -------------           --------------------
        |  Apples   |           |      Apples      |
        |  Bananas  |           |     Bananas      |
        |Watermelons|           |Oranges -Purchased|
        -------------           |   Watermelons    |
                                --------------------
        """
        # Assign the length of the longest item on the list to list_width
        list_width = max(len(s) for s in self.items)
        list_divider = "-" * (list_width + 2)
        print "My Shopping List:"
        print list_divider
        # Loop through the items in the list and assign the length to item_len
        # Find the difference between list_width and item_len to determine the
        # number of spaces that you need to put around the item.
        for item in self.items:  # loop through items
            item_len = len(item)  # assign item_len to the length of each item
            space_diff = list_width - item_len
            spacing_before = spacing_after = " " * (space_diff/2)
            # Create an if statement that determines if space_diff is odd.
            # Change spacing_after to the appropriate number of spaces to keep
            # the list borders lined up when space_diff is odd.
            if (space_diff % 2) != 0:  # check if space_diff is odd
                spacing_after += " "  # change spacing_after
            print "|" + spacing_before + item + spacing_after + "|"
        print list_divider + "\n"

    def add_to_list(self, item):
        if item in self.items:
            return "%s is already on the list!" % item
        elif item + " -Purchased" in self.items:
            return "You already bought %s." % item
        else:
            self.items.append(item)
            return "Added %s to the list." % item

    def remove_from_list(self, item):
        if item in self.items:
            self.items.remove(item)
            return "%s has been removed from the list." % item
        elif item + " -Purchased" in self.items:
            return "You already bought %s." % item
        else:
            return "%s is not on the list." % item

    def purchase_item(self, purchased_item):
        if purchased_item in self.items:
            i = self.items.index(purchased_item)
            self.items[i] += " -Purchased"
            self.show_list()
            return "Purchased % s." % purchased_item
        elif purchased_item + " -Purchased" in self.items:
            return "You already bought %s." % purchased_item
        else:
            return "%s is not on your list!" % purchased_item