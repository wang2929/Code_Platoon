import { useState } from "react";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

export default function CharacterCard({ name, img, id, rmData }) {
  return(
            <Card style={{ width: '10rem' }} bg="black" border="warning">
              <Card.Img variant="top" src={img} />
              <Card.Body>
                <Card.Subtitle>{name}</Card.Subtitle>
                <Button className="btn btn-outline-danger btn-sm" 
                  style={{"bsBtnPaddingY": "5rem", "bsBtnPaddingX": "1rem", "bsBtnFontSize": "1rem"}} onClick={()=>rmData(id)}>
                  remove
                </Button>
              </Card.Body>
            </Card>
    )
}
