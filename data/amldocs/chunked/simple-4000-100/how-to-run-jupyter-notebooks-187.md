|Navigate to another workspace section     |     Running cells are stopped. |

These actions will reset the notebook state and will reset all variables in the notebook.

|Action  |Result  |
|---------|---------| --------|
| Change the kernel | Notebook uses new kernel |
| Switch compute    |     Notebook automatically uses the new compute. |
| Reset compute | Starts again when you try to run a cell |
| Stop compute     |    No cells will run  |
| Open notebook in Jupyter or JupyterLab     |    Notebook opened in a new tab.  |

## Add new kernels

[Use the terminal](how-to-access-terminal.md#add-new-kernels) to create and add new kernels to your compute instance. The notebook will automatically find all Jupyter kernels installed on the connected compute instance.

Use the kernel dropdown on the right to change to any of the installed kernels.  

## Manage packages

Since your compute instance has multiple kernels, make sure use `%pip` or `%conda` [magic functions](https://ipython.readthedocs.io/en/stable/interactive/magics.html), which  install packages into the currently running kernel.  Don't use `!pip` or `!conda`, which refers to all packages (including packages outside the currently running kernel).

### Status indicators

An indicator next to the **Compute** dropdown shows its status.  The status is also shown in the dropdown itself.  

|Color |Compute status |
|---------|---------| 
| Green | Compute running |
| Red |Compute failed | 
| Black | Compute stopped |
|  Light Blue |Compute creating, starting, restarting, setting Up |
|  Gray |Compute deleting, stopping |

An indicator next to the **Kernel** dropdown shows its status.

|Color |Kernel status |
|---------|---------|
|  Green |Kernel connected, idle, busy|
|  Gray |Kernel not connected |

## Find compute details

Find details about your compute instances on the **Compute** page in [studio](https://ml.azure.com).

## Useful keyboard shortcuts
Similar to Jupyter Notebooks, Azure Machine Learning studio notebooks have a modal user interface. The keyboard does different things depending on which mode the notebook cell is in. Azure Machine Learning studio notebooks support the following two modes for a given code cell: command mode and edit mode.

### Command mode shortcuts

A cell is in command mode when there's no text cursor prompting you to type. When a cell is in Command mode, you can edit the notebook as a whole but not type into individual cells. Enter command mode by pressing `ESC` or using the mouse to select outside of a cell's editor area.  The left border of the active cell is blue and solid, and its **Run** button is blue.

   :::image type="content" source="media/how-to-run-jupyter-notebooks/command-mode.png" alt-text="Notebook cell in command mode ":::

| Shortcut                      | Description                          |
| ----------------------------- | ------------------------------------|
| Enter                         | Enter edit mode             |        
| Shift + Enter                 | Run cell, select below         |     
| Control/Command + Enter       | Run cell                            |
| Alt + Enter                   | Run cell, insert code cell below    |
| Control/Command + Alt + Enter | Run cell, insert markdown cell below|
| Alt + R                       | Run all      |                       
| Y                             | Convert cell to code    |                         
| M                             | Convert cell to markdown  |                       
| Up/K                          | Select cell above    |               
| Down/J                        | Select cell below    |               
| A                             | Insert code cell above  |            
| B                             | Insert code cell below   |           
| Control/Command + Shift + A   | Insert markdown cell above    |      
| Control/Command + Shift + B   | Insert markdown cell below   |       
| X                             | Cut selected cell    |               
