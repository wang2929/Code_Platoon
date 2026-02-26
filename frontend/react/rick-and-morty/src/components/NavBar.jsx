import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavbarCollapse from 'react-bootstrap/NavbarCollapse'
import Container from 'react-bootstrap/Container';
import { Link } from 'react-router-dom';

function NavBar() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary" bg="light" data-bs-theme="white">
      <Container>
        <Navbar.Brand as={Link} to="/">Tiffany app</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/about">About</Nav.Link>
          </Nav>
      </Container>
    </Navbar>
  );
}

export default NavBar;