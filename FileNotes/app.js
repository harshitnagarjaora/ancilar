
let notes = JSON.parse(localStorage.getItem("basic_notes")) || [];

function saveNotes() {
  localStorage.setItem("basic_notes", JSON.stringify(notes));
}

function addNote() {
  const title = document.getElementById("noteTitle").value.trim();
  const content = document.getElementById("noteContent").value.trim();

  if (!title) {
    alert("Title is required!");
    return;
  }

  const note = { id: Date.now(), title, content };
  notes.push(note);
  saveNotes();
  renderNotes();

  document.getElementById("noteTitle").value = "";
  document.getElementById("noteContent").value = "";
}

function deleteNote(id) {
  notes = notes.filter(note => note.id !== id);
  saveNotes();
  renderNotes();
}

function copyNote(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert("Note copied!");
  });
}

function viewNote(note) {
  alert("Title: " + note.title + "\nContent: " + note.content);
}

function renderNotes() {
  const list = document.getElementById("notesList");
  list.innerHTML = "";
  notes.forEach(note => {
    const li = document.createElement("li");
    li.textContent = note.title + " ";

    const viewBtn = document.createElement("button");
    viewBtn.textContent = "View";
    viewBtn.onclick = () => viewNote(note);

    const copyBtn = document.createElement("button");
    copyBtn.textContent = "Copy";
    copyBtn.onclick = () => copyNote(note.content || "");

    const delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.onclick = () => deleteNote(note.id);

    li.appendChild(viewBtn);
    li.appendChild(copyBtn);
    li.appendChild(delBtn);
    list.appendChild(li);
  });
}

renderNotes();
