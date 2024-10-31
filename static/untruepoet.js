async function generatePoem() {
    const numLines = document.getElementById("num-lines").value;
    const erraticRhythm = document.getElementById("erratic-rhythm").value;
    const rhymeType = document.getElementById("rhyme-type").value;
    const concreteness = document.getElementById("concreteness").value;
    const rating = document.getElementById("rating").value;
    const seed = document.getElementById("seed").value;

    const response = await fetch("/generate_poem", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ num_lines: numLines, erratic_rhythm: erraticRhythm, rhyme_type: rhymeType, concreteness: concreteness, rating: rating, seed: seed })
    });
    const data = await response.json();
    document.getElementById("poem-output").innerText = data.poem;
}
