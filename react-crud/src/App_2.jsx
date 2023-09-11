import { MouseEventHandler, useEffect, useState } from "react";
import Home from "./components/Home";
import { Routes, Route } from "react-router-dom";
import Note from "./components/Note";
import axios from "axios";
import noteService from './services/notes'
import Notification from "./components/Notification";


const App = () => {
    const [notes, setNotes] = useState(null)
    const [newNote, setNewNotes] = useState('a new note...')
    const [showAll, setShowAll] = useState(true);
    const [errorMessage, setErrorMessage] = useState(null)

    useEffect(() => {
      noteService
        .getAll()
        .then(initialNotes => {
          setNotes(initialNotes)
        })
    }, [])


    const toggleImportanceOf = (id) => {
      const url = `http://localhost:3001/notes/${id}`
      const note = notes.find(n => n.id === id)
      const changedNote = { ...note, important: !note.important }

      noteService
        .update(id, changedNote)
        .then(updatedNote => {
          setNotes(notes.map(n => n.id !== id ? n : updatedNote))
        })
        .catch(error => {
          setErrorMessage(
            `Note ${note.content} was already removed from server`
          )
          setTimeout(() => {
            setErrorMessage(null)
          }, 5000)
        })
        setNotes(notes.filter(n => n.id !== id))

      console.log('importance of ', id, ' needs to be toggled')
    }

  
    const addNote = (event) => {    
        event.preventDefault()   
        const noteObject = {
          content: newNote,
          important: Math.random() < 0.5,
          id: notes.length + 1
        }

        noteService
        .create(noteObject)
        .then(response => {
          setNotes(notes.concat(response))
          setNewNotes('')
        })
    }

    const handleNoteChange = (event) => {
      setNewNotes(event.target.value)
    }

    const notesToShow = showAll ? notes : notes.filter(note => note.important)


    if (!notes) return null;

    return (
      <div>
        <h1>Notes</h1>
        <Notification message={errorMessage} />
        <div>
          <button onClick={() => setShowAll(!showAll)}>
            show {showAll ? 'important' : 'all'}
          </button>
        </div>
        <ul>
          {notesToShow.map(note => 
            <Note 
              key={note.id} 
              note={note} 
              toggleImportance={() => toggleImportanceOf(note.id)}
            />
          )}
        </ul>
        <form onSubmit={addNote}>        
        <input 
            value={newNote}
            onChange={handleNoteChange}
        />
        <button type="submit">save</button>      
        </form>       
    </div>
    )
  }

export default App;
