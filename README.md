# Story-Word-Replacement
This Python script allows you to replace placeholder words in a text file with custom words provided by the user.

## Usage

1. Run the Python script `story_word_replacement.py`.
2. Enter the name of the file containing the story when prompted.
3. The script reads the content of the file and identifies words enclosed within `<` and `>` symbols as placeholders.
4. For each placeholder word found in the story, you will be prompted to enter a replacement word.
5. Once all placeholder words have been replaced, the modified story is displayed.

## Functionality

- The script prompts the user to enter the name of the file containing the story.
- It reads the content of the file and identifies placeholder words enclosed within `<` and `>` symbols.
- For each placeholder word found, the user is prompted to enter a replacement word.
- The script then replaces all occurrences of placeholder words with the corresponding replacement words in the story.
- The modified story is printed to the console.

## Example

Suppose the input file contains the following story:
Upon running the script, you would provide replacements for `<noun>` and `<place>`. For example:
Enter a word for <noun>: cat
Enter a word for <place>: castle

The script would then output:

Once upon a time, there was a cat. The cat lived in a castle.

## Notes

- Placeholder words must be enclosed within `<` and `>` symbols.
- Replacement words can be any string provided by the user.

## Author

This script was created by ACHKHITY YASSINE.

