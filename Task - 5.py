import tkinter as tk
from tkinter import ttk

class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("My Contact Book")

        # Contact list
        self.contacts = []

        # Create widgets
        style = ttk.Style()
        style.configure('W.TButton', font=('calibri', 10, 'bold'), foreground='black', background='#CD6889')

        self.name_label = ttk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = ttk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = ttk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = ttk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = ttk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = ttk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = ttk.Entry(master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = ttk.Button(master, text="Add Contact", style='W.TButton', command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.search_label = ttk.Label(master, text="Search:")
        self.search_label.grid(row=5, column=0, padx=10, pady=10)
        self.search_entry = ttk.Entry(master)
        self.search_entry.grid(row=5, column=1, padx=10, pady=10)
        self.search_button = ttk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=5, column=2, padx=10, pady=10)

        self.contact_list = ttk.Treeview(master)
        self.contact_list['columns'] = ('Name', 'Phone')
        self.contact_list.heading('#0', text='ID', anchor='w')
        self.contact_list.heading('Name', text='Name', anchor='w')
        self.contact_list.heading('Phone', text='Phone', anchor='w')
        self.contact_list.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        self.update_button = ttk.Button(master, text="Update Contact", style='W.TButton', command=self.update_contact)
        self.update_button.grid(row=7, column=0, padx=10, pady=10)


        self.delete_button = ttk.Button(master, text="Delete Contact", style='W.TButton', command=self.delete_contact)
        self.delete_button.grid(row=7, column=1, padx=10, pady=10)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
            self.contacts.append(contact)
            self.contact_list.insert('', 'end', text=len(self.contacts), values=(name, phone))
            self.clear_entries()

    def search_contact(self):
        search_term = self.search_entry.get()
        self.contact_list.delete(*self.contact_list.get_children())
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                self.contact_list.insert('', 'end', text=self.contacts.index(contact) + 1, values=(contact['name'], contact['phone']))

    def update_contact(self):
        selected = self.contact_list.focus()
        if selected:
            index = int(self.contact_list.item(selected)['text']) - 1
            self.contacts[index]['name'] = self.name_entry.get()
            self.contacts[index]['phone'] = self.phone_entry.get()
            self.contacts[index]['email'] = self.email_entry.get()
            self.contacts[index]['address'] = self.address_entry.get()
            self.contact_list.item(selected, values=(self.contacts[index]['name'], self.contacts[index]['phone']))
            self.clear_entries()

    def delete_contact(self):
        selected = self.contact_list.focus()
        if selected:
            index = int(self.contact_list.item(selected)['text']) - 1
            self.contacts.pop(index)
            self.contact_list.delete(selected)
            self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
root.config(bg="#3D9140")
app = ContactBook(root)
root.mainloop()
