# vibevision

## Inspiration
VibeVision was inspired by the idea of turning everyday objects into musical instruments without the extra cost. We wanted to create something that would allow users to point at objects around them and generate a sound that fits the vibe of that object. For example, pointing at a cup and hearing a bass drop, or pointing at a book and getting a soothing sound. We thought it would be cool to blend everyday life with music, allowing people to compose their own soundtrack based on the world around them.
We also have an experimental version where an AI generated melody will be played based on the object! 

## What it does
VibeVision uses the EfficientDet-Lite0 model from MediaPipe to perform live-streaming object detection. It identifies objects in the real world, then sends a request to OpenAI's GPT-4o Mini model to ask for the type of sound associated with that object. Once OpenAI's GPT-4o Mini model responds, the app queries an open-source sound library called Freesound for the corresponding audio which is then played.
We also have an experimental version where an AI generated melody will be played based on the object! This uses BeatOven AI which is a text to music AI generator. 

## How we built it
We used MediaPipe for object detection, which provided real-time object recognition and tracking objects through live video. The object detection results were passed to OpenAI's GPT-4o Mini model, where we crafted prompts to get relevant sounds. To integrate sound, we leveraged the Freesound API, pulling from its extensive collection of sound effects. We built the app in Python with a combination of Flask for the back-end, React for the front-end, and Github for classic version control.
For the experimental version, we utilize Beatoven AI's APIs to generate songs. 
TLDR: We ran a model, put a bunch of APIs together, and made something beautiful!

## Challenges we ran into
One of the biggest challenges we faced was integrating MediaPipe for object detection. 
Fun fact: Mediapipe is not compatible with Apple M1 clips which is something we learned the hard way! 
As we went along, there were tons of issues with handling the real-time nature of the app. Things like optimization to reduce latency between the object detection and sound playback, making sure we don't hit rate limits, figuring out what MediaPipe is and is not capable of with poor documentation.
Also, APIs are expensive :(

## Accomplishments that we're proud of
We are both graduating this semester and we have been going to Brickhack since we got here. This means, this hackathon is our last one at RIT which is bittersweet but that's ok.
As for the project, we integrated a ton of random things and dealt with so many random issues. The thing we are most proud of is honestly getting the whole thing to work when we both had different halves of the app working at all times. 
To us, this feels like a good ending to our college hackathon experience!

## What we learned
Honestly, MediaPipe is cool and Computer Vision is cooler but it's hard and we don't envy that. As many would agree, CORS sucks but we recognize why it's important! Overall, every time we did anything there would be 50000 errors or hidden ones that wouldn't really show themselves. So, we had to do a lot more sleuthing to figure out why stuff wasn't working but #problem-solving.

## What's next for VibeVision
If we ever go farther with this, we would like to:
- Be able to have multiple objects & a delay between the sounds
- Be able to choose an instrument and assign it to an object
- Be able to choose a vibe and have sounds associated to that vibe
- Introduce movement?
