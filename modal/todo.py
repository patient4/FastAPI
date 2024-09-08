from pydantic import BaseModel, Field

class Todo(BaseModel):
    """
    Represents a Todo item with essential details.
    
    Attributes:
        subject (str): The subject or category of the todo item.
        title (str): The title of the todo item.
        description (str): A detailed description of the todo item.
    """
    subject: str = Field(..., example="Work", description="The subject or category of the todo item.")
    title: str = Field(..., example="Complete Report", description="The title of the todo item.")
    description: str = Field(..., example="Prepare the financial report for Q3", description="A detailed description of the todo item.")

    def __str__(self):
        """
        Returns a string representation of the Todo item.
        
        Returns:
            str: A string describing the Todo item.
        """
        return f"Todo(subject={self.subject}, title={self.title}, description={self.description})"
