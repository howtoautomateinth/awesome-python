# An in-memory stream for text I/O
# StringIO gives you file-like access to strings, so you can use an existing module that deals with a file and change almost nothing and make it work with strings.
# StringIO is also helpful in writing a file directly into S3
import io

output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()
print(contents)

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
