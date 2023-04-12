1. To make it easier to work with the image locally, you can use the following command to add a tag for this image. Replace `myimagepath` in the following command with the location value from the previous step.

    ```bash
    docker tag myimagepath debug:1
    ```

    For the rest of the steps, you can refer to the local image as `debug:1` instead of the full image path value.

### Debug the service

> [!TIP]
> If you set a timeout for the debugpy connection in the `score.py` file, you must connect VS Code to the debug session before the timeout expires. Start VS Code, open the local copy of `score.py`, set a breakpoint, and have it ready to go before using the steps in this section.
>
> For more information on debugging and setting breakpoints, see [Debugging](https://code.visualstudio.com/Docs/editor/debugging).

1. To start a Docker container using the image, use the following command:

    ```bash
    docker run -it --name debug -p 8000:5001 -p 5678:5678 -v <my_local_path_to_score.py>:/var/azureml-app/score.py debug:1 /bin/bash
    ```

    This command attaches your `score.py` locally to the one in the container. Therefore, any changes made in the editor are automatically reflected in the container

2. For a better experience, you can go into the container with a new VS code interface. Select the `Docker` extention from the VS Code side bar, find your local container created, in this documentation its `debug:1`. Right-click this container and select `"Attach Visual Studio Code"`, then a new VS Code interface will be opened automatically, and this interface shows the inside of your created container.

    ![The container VS Code interface](./media/how-to-troubleshoot-deployment/container-interface.png)

3. Inside the container, run the following command in the shell

    ```bash
    runsvdir /var/runit
    ```
    Then you can see the following output in the shell inside your container:

    ![The container run console output](./media/how-to-troubleshoot-deployment/container-run.png)

4. To attach VS Code to debugpy inside the container, open VS Code, and use the F5 key or select __Debug__. When prompted, select the __Azure Machine Learning Deployment: Docker Debug__ configuration. You can also select the __Run__ extention icon from the side bar, the __Azure Machine Learning Deployment: Docker Debug__ entry from the Debug dropdown menu, and then use the green arrow to attach the debugger.

    ![The debug icon, start debugging button, and configuration selector](./media/how-to-troubleshoot-deployment/start-debugging.png)
    
    After you select the green arrow and attach the debugger, in the container VS Code interface you can see some new information:
    
    ![The container debugger attached information](./media/how-to-troubleshoot-deployment/debugger-attached.png)
    
    Also, in your main VS Code interface, what you can see is following:

    ![The VS Code breakpoint in score.py](./media/how-to-troubleshoot-deployment/local-debugger.png)

And now, the local `score.py` which is attached to the container has already stopped at the breakpoints where you set. At this point, VS Code connects to debugpy inside the Docker container and stops the Docker container at the breakpoint you set previously. You can now step through the code as it runs, view variables, etc.

For more information on using VS Code to debug Python, see [Debug your Python code](https://code.visualstudio.com/docs/python/debugging).

### Stop the container

To stop the container, use the following command:

```bash
docker stop debug
```

## Next steps

Now that you've set up VS Code Remote, you can use a compute instance as remote compute from VS Code to interactively debug your code. 

Learn more about troubleshooting:

* [Local model deployment](./v1/how-to-troubleshoot-deployment-local.md)
* [Remote model deployment](./v1/how-to-troubleshoot-deployment.md)
* [Machine learning pipelines](v1/how-to-debug-pipelines.md)
* [ParallelRunStep](v1/how-to-debug-parallel-run-step.md)
