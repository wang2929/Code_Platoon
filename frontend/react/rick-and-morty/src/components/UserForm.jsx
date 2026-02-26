import { useState } from 'react';
import axios from 'axios';
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Stack from 'react-bootstrap/Stack'

export default function UserForm({ setName }) {

    const handleSubmit = (e) => {
        e.preventDefault()
        setName(e.target[0].value)
        e.target[0].value = ""
    }

    return (
    <div className="flex justify-center"> 
        <Form onSubmit={(e)=>handleSubmit(e)}>
            <Stack direction="horizontal" gap={3}>
                <Form.Control 
                className="me-auto" 
                placeholder="type in a character name:"
                />
                <Button variant="secondary" type="submit">Submit</Button>
            </Stack>
        </Form>
    </div>
  )
}
