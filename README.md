<h1>Door Mat Pattern Generator </h1>
<p>This Python script generates a decorative door mat pattern based on the specified dimensions. The door mat includes a pattern of .|. and a "WELCOME" message in the center. The dimensions must meet specific constraints for the pattern to be valid.</p>
<h2>How It Works</h2>
<ul>
  <li>The user provides two integers:
    <ul>
      <li>n: The number of rows (must be odd and greater than 1).</li>
      <li>m: The number of columns (must be exactly 3 times n</li>
    </ul>
  </li>
  <li>
      The script validates the input. If the conditions are met, it generates the door mat pattern with the following structure:
      <ul>
        <li>A top section with increasing .|. patterns.</li>
        <li>A middle section displaying "WELCOME".</li>
        <li>A bottom section mirroring the top section.</li>
      </ul>
  </li>
  <li>
    If the constraints are not met, the script displays an error message.
  </li>
</ul>
<h2>Input Format</h2>
<p>The script prompts the user to enter the values for n and m in the format:</p>
<ul>
  <li>Enter n & m like(n,m) : <value_n>,<value_m>
</li>
</ul>
<h2>Constraints</h2>
<ul>
  <li>n must be odd and greater than 1.</li>
  <li>m must be equal to 3 * n.</li>
</ul>



