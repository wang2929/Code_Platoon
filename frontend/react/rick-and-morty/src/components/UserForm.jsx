import { useState } from 'react';
import axios from 'axios';
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Stack from 'react-bootstrap/Stack'

export default function UserForm({ charName, setCharName, filterData }) {
    const [searchText, setSearchText] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        filterData(1, charName)
        setSearchText("")
    }

    return (
    <div className="flex justify-center"> 
        <Form onSubmit={(e)=>handleSubmit(e)}>
            <Stack direction="horizontal" gap={3}>
                <Form.Control 
                className="me-auto" 
                placeholder="type in a character name:"
                value={charName}
                onChange={(e)=> { 
                    setCharName(e.target.value) 
                }}
                />
                <Button variant="secondary" type="submit">Submit</Button>
            </Stack>
        </Form>
    </div>
  )
}
