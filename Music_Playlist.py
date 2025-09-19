class Node:
   def __init__(self, data):
     self.data = data
     self.next = None
class Playlist:
   def __init__(self):
     self.head = None
   def insert_beginning(self, song):
    new_node = Node(song)
    new_node.next = self.head
    self.head = new_node
    print(f"'{song}' inserted at beginning.")
   def insert_end(self, song):
    new_node = Node(song)
    if self.head is None:
      self.head = new_node
      print(f"'{song}' inserted as the first song.")
      return
    temp = self.head
    while temp.next:
       temp = temp.next
    temp.next = new_node
    print(f"'{song}' inserted at end.")
   def insert_middle(self, song, position):
     if position == 1:
        self.insert_beginning(song)
        return
     new_node = Node(song)
     temp = self.head
     for _ in range(position - 2):
       if temp is None:
         print("Position out of range.")
         return
       temp = temp.next
       if temp is None:
         print("Position out of range.")
         return
     new_node.next = temp.next
     temp.next = new_node
     print(f"'{song}' inserted at position {position}.")
   def delete_song(self, song):
     curr = self.head
     prev = None
     while curr:
       if curr.data == song:
         if prev is None:
            self.head = curr.next
         else:
            prev.next = curr.next
         print(f"'{song}' deleted from playlist.")
         return True
       prev = curr
       curr = curr.next
     print(f"'{song}' not found in playlist.")
     return False
   def find_song(self, song):
    temp = self.head
    while temp:
      if temp.data == song:
         print(f"'{song}' found in playlist.")
         return True
      temp = temp.next
    print(f"'{song}' not found in playlist.")
    return False
   def display_playlist(self):
      temp = self.head
      if not temp:
           print("Playlist is empty.")
           return
      print("Playlist:")
      while temp:
         print(f"-> {temp.data}", end=" ")
         temp = temp.next
      print()
playlist = Playlist()
while True:
  print("\n--- Music Playlist Menu ---")
  print("1. Insert song at beginning")
  print("2. Insert song at end")
  print("3. Insert song at position")
  print("4. Delete song")
  print("5. Find song")
  print("6. Display playlist")
  print("7. Exit")
  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid input. Enter a number.")
    continue
  if choice == 1:
     song = input("Enter song name to insert at beginning: ")
     playlist.insert_beginning(song)
  elif choice == 2:
     song = input("Enter song name to insert at end: ")
     playlist.insert_end(song)
  elif choice == 3:
     song = input("Enter song name to insert: ")
     try:
       position = int(input("Enter position to insert: "))
       playlist.insert_middle(song, position)
     except ValueError:
       print("Invalid position.")
  elif choice == 4:
    song = input("Enter song name to delete: ")
    playlist.delete_song(song)
  elif choice == 5:
    song = input("Enter song name to find: ")
    playlist.find_song(song)
  elif choice == 6:
    playlist.display_playlist()
  elif choice == 7:
    print("Exiting program...")
    break
  else:
    print("Invalid choice. Try again.")
