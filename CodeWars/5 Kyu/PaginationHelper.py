class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
      self.pages = (len(self.collection)//self.items_per_page)+1
      return self.pages
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      self.items_last_page = len(self.collection) - ((self.pages - 1) * self.items_per_page)
      self.itemscount = self.items_last_page if (page_index+1) == self.pages else self.items_per_page
      return self.itemscount if 0 < page_index < self.pages else -1
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      return (item_index//self.items_per_page) if item_index in range(len(self.collection)) else -1