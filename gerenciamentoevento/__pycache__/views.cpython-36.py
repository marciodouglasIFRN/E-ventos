3
�\:  �               @   s<   d dl mZ d dlmZ dd� Zdd� Zdd� Zd	d
� ZdS )�    )�HttpResponse)�renderc             C   s
   t | d�S )Nz	home.html)r   )�request� r   �D/home/marcio/django/gerenciamentoevento/gerenciamentoevento/views.py�home   s    r   c             C   s
   t | d�S )Nz
about.html)r   )r   r   r   r   �about   s    r   c             C   s
   t | d�S )Nzpromoter.html)r   )r   r   r   r   �promoter
   s    r	   c             C   s
   t | d�S )Nzregister.html)r   )r   r   r   r   �register   s    r
   N)�django.httpr   Zdjango.shortcutsr   r   r   r	   r
   r   r   r   r   �<module>   s
   