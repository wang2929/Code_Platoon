import Pagination from 'react-bootstrap/Pagination';

export default function PaginationWithEllipsis({ page, endPage, updatePage }) {
    let items = []
    const paginationItems = (start, end, active) => {
        for (let number = start; number <= end; number++) {
            items.push(
                <Pagination.Item key={number} 
                                onClick={(e) => updatePage(e.target.text)} 
                                active={number === active}>
                    {number}
                </Pagination.Item>
            )
        }
    }

    if (page != 1) {
        items.push(<Pagination.First onClick={() => updatePage(1)}/>)
        items.push(<Pagination.Prev onClick={() => (page-1) > 0 ? updatePage(page-1) : updatePage(1)}/>)
    }
    if (endPage > 9) {
        if (page < 3) {
            paginationItems(1, 5, page)
            items.push(<Pagination.Ellipsis key={"ellipsis"}/>)
            items.push(<Pagination.Item key={endPage} onClick={(e) => updatePage(e.target.text)}>{endPage}</Pagination.Item>)
        }
        else if (page < (endPage-3)) {
            items.push(<Pagination.Item key={1} onClick={(e) => updatePage(e.target.text)}>1</Pagination.Item>)
            items.push(<Pagination.Ellipsis key={"before-ellipsis"}/>)
            paginationItems(page-2, page+2, page)
            items.push(<Pagination.Ellipsis key={"after-ellipsis"}/>)
            items.push(<Pagination.Item key={endPage} onClick={(e) => updatePage(e.target.text)}>{endPage}</Pagination.Item>)
        }
        else {
            items.push(<Pagination.Item key={1} onClick={(e) => updatePage(e.target.text)}>1</Pagination.Item>)
            items.push(<Pagination.Ellipsis key={"ellipsis"}/>)
            paginationItems(endPage-5, endPage, active)
        }
    } else {
        paginationItems(page, endPage)
    }
    if (page != endPage) {
        items.push(<Pagination.Next onClick={() => (page+1 < end) ? updatePage(page+1) : updatePage(end)}/>)
        items.push(<Pagination.Last onClick={() => updatePage(end)}/>)
    }
    
    return (
        <Pagination>{items}</Pagination>
    );
}