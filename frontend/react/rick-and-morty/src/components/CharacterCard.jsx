import { useState } from "react";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

export default function CharacterCard({ name, img, id, rmData }) {
  return(
            <Card className="char-cards" style={{ width: '10rem' }} >
              <Card.Img variant="top" src={img} />
              <Card.Body>
                <Card.Text>{name}</Card.Text>
                <Button className="btn btn-outline-danger btn-sm" 
                  style={{"bsBtnPaddingY": "5rem", "bsBtnPaddingX": "1rem", "bsBtnFontSize": "1rem"}} onClick={()=>rmData(id)}>
                  remove
                </Button>
              </Card.Body>
            </Card>
    )
}
