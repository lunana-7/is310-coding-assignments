"use strict";

const form = document.querySelector("#movie-form");
const review = document.querySelector("#review");
const preview = document.querySelector("#preview");
const status = document.querySelector("#status");
const download = document.querySelector("#download");
const records = [];
const fields = ["title", "director", "year", "cultural_note"];
const labels = ["Title", "Director", "Year", "Cultural note"];
let pendingRecord = null;

form.elements.year.max = new Date().getFullYear();

// Native required validation also needs this check for whitespace-only values.
for (const name of fields) {
  form.elements[name].addEventListener("input", () => {
    form.elements[name].setCustomValidity("");
  });
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  for (const name of fields) {
    const input = form.elements[name];
    input.setCustomValidity(input.value.trim() ? "" : "Please enter a value.");
  }
  if (!form.reportValidity()) return;
  pendingRecord = {
    title: form.elements.title.value.trim(),
    director: form.elements.director.value.trim(),
    year: Number(form.elements.year.value),
    cultural_note: form.elements.cultural_note.value.trim(),
  };
  preview.replaceChildren();
  fields.forEach((field, index) => {
    const term = document.createElement("dt");
    term.textContent = labels[index];
    const value = document.createElement("dd");
    value.textContent = pendingRecord[field];
    preview.append(term, value);
  });
  form.hidden = true;
  review.hidden = false;
  document.querySelector("#confirm").focus();
});

document.querySelector("#edit").addEventListener("click", () => {
  pendingRecord = null;
  review.hidden = true;
  form.hidden = false;
  form.elements.title.focus();
});

document.querySelector("#confirm").addEventListener("click", () => {
  if (!pendingRecord) return;
  records.push(pendingRecord);
  const row = document.createElement("tr");
  fields.forEach((field) => {
    const cell = document.createElement("td");
    // Treat user input as text, even if it contains HTML characters.
    cell.textContent = pendingRecord[field];
    row.append(cell);
  });
  document.querySelector("#records").append(row);
  pendingRecord = null;
  review.hidden = true;
  form.hidden = false;
  form.reset();
  download.disabled = records.length < 2;
  status.textContent = records.length < 2
    ? "1 record. Confirm one more to download."
    : `${records.length} records. Ready to download. You can also add more.`;
  form.elements.title.focus();
});

download.addEventListener("click", () => {
  if (records.length < 2) return;
  const blob = new Blob([JSON.stringify(records, null, 2) + "\n"], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "movies_web.json";
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
