# Frame to Video
* Creates a video from the given frames.

## Project Layout
    frames_to_video/
        main.py    # Video generated python file.
        README.md

## Functions
    frames_to_video/
        main.py 
            def create_video() # Creates a video in the desired format from the given frames.

## Function Descriptions
### create video
`def create_video(frames_file)`

 Sorts the given frames from smallest to largest according to their names and produces a video in the desired format.
 
*ARGS*
* **frames_file:** The folder where the frames to create the video are in.


*EXAMPLE USAGE*

    create_video(
        frames_file = ''
    )
