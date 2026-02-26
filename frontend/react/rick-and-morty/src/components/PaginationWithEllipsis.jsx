import Pagination from 'react-bootstrap/Pagination';

export default function PaginationWithEllipsis({ page, endPage, updatePage }) {
    let items = []

    const paginationItems = (items, start, end, active) => {
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

    if (endPage > 9) {
        if (page != 1) {
            items.push(<Pagination.First key="first" onClick={() => updatePage(1)}/>)
            items.push(<Pagination.Prev key="prev" onClick={() => (page-1) > 0 ? updatePage(page-1) : updatePage(1)}/>)
        }
        if (page < 3) {
            paginationItems(items, 1, 5, page)
            items.push(<Pagination.Ellipsis key={"ellipsis"}/>)
            items.push(<Pagination.Item key={endPage} onClick={(e) => updatePage(e.target.text)}>{endPage}</Pagination.Item>)
        }
        else if (page < (endPage-3)) {
            items.push(<Pagination.Item key={1} onClick={(e) => updatePage(e.target.text)}>1</Pagination.Item>)
            items.push(<Pagination.Ellipsis key={"before-ellipsis"}/>)
            console.log(`Before pagination: ${page-2} to ${page+2} with ${page} active`)
            paginationItems(items, page-2, page+2, page)
            items.push(<Pagination.Ellipsis key={"after-ellipsis"}/>)
            items.push(<Pagination.Item key={endPage} onClick={(e) => updatePage(e.target.text)}>{endPage}</Pagination.Item>)
        }
        else {
            items.push(<Pagination.Item key={1} onClick={(e) => updatePage(e.target.text)}>1</Pagination.Item>)
            items.push(<Pagination.Ellipsis key={"ellipsis"}/>)
            paginationItems(items, endPage-5, endPage, active)
        }
        if (page != endPage) {
            items.push(<Pagination.Next key="next" onClick={() => (page+1 < endPage) ? updatePage(page+1) : updatePage(endPage)}/>)
            items.push(<Pagination.Last key="last" onClick={() => updatePage(endPage)}/>)
        }
    } else {
        if (page != 1) {
            items.push(<Pagination.Prev key="prev" onClick={() => (page-1) > 0 ? updatePage(page-1) : updatePage(1)}/>)
        }
        paginationItems(items, 1, endPage, page)
        if (page != endPage) {
            items.push(<Pagination.Next key="next" onClick={() => (page+1 < endPage) ? updatePage(page+1) : updatePage(endPage)}/>)
        }
    }
    
    return (
        <Pagination>{items}</Pagination>
    );
}