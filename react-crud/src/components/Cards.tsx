import { Card, CardActionArea, CardContent, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";

interface Info {
    title: string,
    description : string
}

const Cards = ({title, description} : Info) => {
    const navigate = useNavigate();

    const handleClick = () => {
        // Push to designated page
        const link = '/playground/' + title.toLowerCase()
        navigate(link);
    };

    return (
        <Card sx={{ maxWidth: 400}}>
            <CardActionArea onClick={() => handleClick()}>
                <CardContent>
                    <Typography gutterBottom variant="h5" component={"div"}>
                        {title}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {description}
                    </Typography>
                </CardContent>
            </CardActionArea>
        </Card>
    )
}

export default Cards;